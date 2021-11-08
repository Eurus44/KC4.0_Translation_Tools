import React, { useEffect, useState } from 'react';
import {
	Row,
	Col,
} from 'react-bootstrap';
import PropTypes from 'prop-types';
import styles from './translateStyle.module.css';
import { Button, Fab, } from '@mui/material';
import { connect } from 'react-redux';
import { STATE } from '../../redux/reducers/translateReducer';
import {
	changeSourceText,
	changeTargetText,
	changeSource,
} from '../../redux/actions/translateAction';
import {
	changeFileDocument, changeFileAudio, changeOutput
} from '../../redux/actions/translateFileAction';
import InsertDriveFileIcon from '@mui/icons-material/InsertDriveFile';
import AlbumIcon from '@mui/icons-material/Album';
import TranslateIcon from '@mui/icons-material/Translate';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import { useTranslation } from 'react-i18next';
import ScrollTop from '../../components/ScrollTop';
import TranslateFileDocumentOutput from './components/TranslateFileDocumentOutput';
import TranslateFileAudioOutput from './components/TranslateFileAudioOutput';
import TranslationChooselang from './components/TranslationChooselang';
import TranslateOutput from './components/TranslateOutput';
import TranslateInput from './components/TranslateInput';
import { TRANSLATE_TYPE } from '../../constants/common';
import TranslateFileDocumentInput from './components/TranslateFileDocumentInput';
import TranslateFileAudioInput from './components/TranslateFileAudioInput';
import authHoc from '../../hocs/authHoc';

function Index(props) {
	const { translationState, translationFileState } = props;
	const { t } = useTranslation();
	const [translateType, setTranslateType] = useState(TRANSLATE_TYPE.plainText);

	/**
	 * @description useEffect cho việc check kết quả và báo noti cho 
	 * người dùng
	 */
	useEffect(() => {
		switch (translationState.currentState) {
		case STATE.SUCCESS:
			break;
		case STATE.FAILURE:
			break;
		default:
			break;
		}
	}, [translationState.currentState]);

	/**
	 * @description useEffect cho việc check kết quả và báo noti cho 
	 * người dùng
	 */
	useEffect(() => {
		switch (translationFileState.currentState) {
		case STATE.SUCCESS:
			break;
		case STATE.FAILURE:
			break;
		default:
			break;
		}
	}, [translationFileState.currentState]);


	const renderOutput = () => {
		switch (translateType) {
		case TRANSLATE_TYPE.plainText:
			return <TranslateOutput translateType={translateType} />;
		case TRANSLATE_TYPE.document:
			return <TranslateFileDocumentOutput translateType={translateType} />;
		case TRANSLATE_TYPE.audio:
			return <TranslateFileAudioOutput translateType={translateType} />;
		}
	};

	const renderInput = () => {
		switch (translateType) {
		case TRANSLATE_TYPE.plainText:
			return <TranslateInput translateType={translateType} />;
		case TRANSLATE_TYPE.document:
			return <TranslateFileDocumentInput translateType={translateType} />;
		case TRANSLATE_TYPE.audio:
			return <TranslateFileAudioInput translateType={translateType} />;
		}
	};

	return (
		<>
			<div className={styles.outerContainer}>
				<div className={styles.outerTab} >
					<Button
						onClick={() => {
							setTranslateType(TRANSLATE_TYPE.plainText);
							// props.changeOutput(null);
						}}
						style={{ fontWeight: 'bold', marginRight: '20px', display: 'flex', backgroundColor: 'white', color: 'grey', borderColor: 'grey' }}
						variant={translateType == TRANSLATE_TYPE.plainText ? 'outlined' : null}
						disabled={translationState.currentState === STATE.LOADING || translationFileState.currentState === STATE.LOADING}
					>
						<div style={{ paddingRight: 5, alignContent: 'center' }}>
							<TranslateIcon />
						</div>
						{t('Translate.vanban')}
					</Button>
					
					<Button
						onClick={() => {
							setTranslateType(TRANSLATE_TYPE.document);
							if (props.translationState.translateCode.sourceLang === null) props.changeSource('en');
							// props.changeTargetText('');
							// props.changeSourceText('');
							// props.changeOutput(null);
						}}
						style={{ fontWeight: 'bold', marginRight: '20px', display: 'flex', backgroundColor: 'white', color: 'grey', borderColor: 'grey' }}
						variant={translateType == TRANSLATE_TYPE.document ? 'outlined' : null}
						disabled={translationState.currentState === STATE.LOADING || translationFileState.currentState === STATE.LOADING}
					>
						<div style={{ paddingRight: 5, alignContent: 'center' }}>
							<InsertDriveFileIcon />
						</div>
						{t('Translate.tailieu')}
					</Button>

					<Button
						onClick={() => {
							setTranslateType(TRANSLATE_TYPE.audio);
							if (props.translationState.translateCode.sourceLang === null) props.changeSource('en');
							// props.changeTargetText('');
							// props.changeSourceText('');
							// props.changeFile(null);
							// props.changeOutput(null);
						}}
						style={{ fontWeight: 'bold', marginRight: '20px', display: 'flex', backgroundColor: 'white', color: 'grey', borderColor: 'grey' }}
						variant={translateType == TRANSLATE_TYPE.audio ? 'outlined' : null}
						disabled={translationState.currentState === STATE.LOADING || translationFileState.currentState === STATE.LOADING}
					>
						<div style={{ paddingRight: 5, alignContent: 'center' }}>
							<AlbumIcon />
						</div>
						{t('Translate.amthanh')}
					</Button>
				</div>

				<div className={styles.content} >
					{/* ChooseLang */}
					<TranslationChooselang translateType={translateType} />
					{/* Box translate */}
					<Col md={12} className={styles.boxTranslate}>
						<Row style={{ minHeight: '150px' }}>
							{/* Input of translation */}
							{renderInput()}
							{/* Output of translation */}
							{renderOutput()}
						</Row>
					</Col>
				</div>

				{/* <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 5 }}>
					<button onClick={() => { }} style={{ backgroundColor: '#fff', borderWidth: 0, color: '#63676C', fontStyle: 'italic', fontSize: 13 }}>
						Gửi phản hồi
					</button>
				</div> */}
				<ScrollTop {...props}>
					<Fab color="primary" size="medium" aria-label="scroll back to top">
						<KeyboardArrowUpIcon />
					</Fab>
				</ScrollTop>
			</div>
		</>
	);
}

Index.propTypes = {
	translationState: PropTypes.object,
	translationFileState: PropTypes.object,
	changeSourceText: PropTypes.func,
	changeTargetText: PropTypes.func,
	changeFile: PropTypes.func,
	changeOutput: PropTypes.func,
	changeSource: PropTypes.func,
};

const mapStateToProps = (state) => ({
	translationState: state.translateReducer,
	translationFileState: state.translateFileReducer
});

const mapDispatchToProps = {
	changeSource,
	changeSourceText,
	changeTargetText,
	changeFileDocument, 
	changeFileAudio,
	changeOutput,
};

export default connect(mapStateToProps, mapDispatchToProps)(authHoc(Index));